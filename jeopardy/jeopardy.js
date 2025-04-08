const BASE_API_URL = "https://rithm-jeopardy.herokuapp.com/api/";
const NUM_CATEGORIES = 6; // Number of categories to display
const NUM_CLUES_PER_CAT = 5; // Number of clues per category

let score = 0; // Initialize the score

// Function to update the score display
function updateScoreDisplay() {
  $("#score").text(`Score: ${score}`);
}

// categories is the main data structure for the app; it looks like this:

//  [
//    { title: "Math",
//      clues: [
//        {question: "2+2", answer: 4, showing: null},
//        {question: "1+1", answer: 2, showing: null}
//        ...
//      ],
//    },
//    { title: "Literature",
//      clues: [
//        {question: "Hamlet Author", answer: "Shakespeare", showing: null},
//        {question: "Bell Jar Author", answer: "Plath", showing: null},
//        ...
//      ],
//    },
//    ...
//  ]

let categories = [];

/** Get NUM_CATEGORIES random category from API.
 *
 * Returns array of category ids
 */

async function getCategoryIds() {
  // ask for 100 categories (per instructions), so that the api can pick a random one
  let response = await axios.get(`${BASE_API_URL}categories`, {
    params: { count: 100 }
  });
  let catIds = response.data.map(c => c.id);
  if (catIds.length < NUM_CATEGORIES) {
    throw new Error(`Not enough categories available. Found ${catIds.length}, but need ${NUM_CATEGORIES}.`);
  }
  return _.sampleSize(catIds, NUM_CATEGORIES);
}

/** Return object with data about a category:
 *
 *  Returns { title: "Math", clues: clue-array }
 *
 * Where clue-array is:
 *   [
 *      {question: "Hamlet Author", answer: "Shakespeare", showing: null, value: 200},
 *      {question: "Bell Jar Author", answer: "Plath", showing: null, value: 400},
 *      ...
 *   ]
 */

async function getCategory(catId) {
  let response = await axios.get(`${BASE_API_URL}category`, {
    params: { id: catId }
  });
  let cat = response.data;
  let randomClues = _.sampleSize(cat.clues, NUM_CLUES_PER_CAT).map(c => ({
    question: c.question,
    answer: c.answer,
    showing: null
  }));
  return { title: cat.title, clues: randomClues };
}

/** Fill the HTML table#jeopardy with the categories & cells for questions.
 *
 * - The <thead> should be filled w/a <tr>, and a <td> for each category
 * - The <tbody> should be filled w/NUM_QUESTIONS_PER_CAT <tr>s,
 *   each with a question for each category in a <td>
 *   (initally, just show a "?" where the question/answer would go.)
 */

async function fillTable() {
  hideLoadingView();

  // Add row with headers for categories
  let $tr = $("<tr>");
  for (let category of categories) {
    $tr.append($("<th>").text(category.title));
  }
  $("#jeopardy thead").append($tr);

  // Add rows with questions for each category
  $("#jeopardy tbody").empty();
  for (let clueIdx = 0; clueIdx < NUM_CLUES_PER_CAT; clueIdx++) {
    let $tr = $("<tr>");
    for (let catIdx = 0; catIdx < NUM_CATEGORIES; catIdx++) {
      $tr.append(
        $("<td>")
          .attr("id", `${catIdx}-${clueIdx}`)
          .append($("<i>").addClass("fas fa-question-circle fa-3x"))
      );
    }
    $("#jeopardy tbody").append($tr);
  }
}

//** Handle clicking on a clue cell:
function handleClick(evt) {
  let $tgt = $(evt.target).closest("td"); // Ensure we get the <td> element
  let id = $tgt.attr("id");
  let [catId, clueId] = id.split("-");
  let clue = categories[catId].clues[clueId];

  // Ignore clicks if the answer is already shown or the cell is disabled
  if (clue.showing === "answer" || $tgt.hasClass("disabled")) {
    return;
  }

  // Show the question and input field if not already shown
  if (!clue.showing) {
    clue.showing = "question";
    displayQuestion($tgt, clue);
  }
}

function displayQuestion($cell, clue) {
  $cell.html(`
    <div>${clue.question}</div>
    <input type="text" class="answer-input" placeholder="Your answer">
    <button class="submit-answer">Submit</button>
  `);

  // Attach event listener for the "Submit" button
  $cell.find(".submit-answer").on("click", function () {
    handleAnswerSubmission($cell, clue);
  });
}

function handleAnswerSubmission($cell, clue) {
  let userAnswer = $cell.find(".answer-input").val().trim().toLowerCase();
  let correctAnswer = clue.answer.toString().trim().toLowerCase();
// sanitizes both user input and correct answer to avoid case sensitivity issues and extra spaces
  if (userAnswer === correctAnswer) {
    score += 10; // Increment score for correct answer
    updateScoreDisplay(); // Update the score display
    $cell.html(`<div class="correct">Correct!</div>`);
  } else {
    $cell.html(`<div class="incorrect">Incorrect! The answer was: ${clue.answer}</div>`);
  }

  // Mark the cell as answered and disable further interaction
  clue.showing = "answer";
  $cell.addClass("disabled");
}

/** Wipe the current Jeopardy board, show the loading spinner,
 * and update the button used to fetch data.
 */

function showLoadingView() {
  // clear the board
  $("#jeopardy thead").empty();
  $("#jeopardy tbody").empty();

  // show the loading icon
  $("#spin-container").show();
  $("#start")
    .addClass("disabled")
    .text("Loading...");
}

/** Remove the loading spinner and update the button used to fetch data. */

function hideLoadingView() {
  $("#start")
    .removeClass("disabled")
    .text("Restart!");
  $("#spin-container").hide();
}

/** Start game:
 *
 * - generates random category Ids
 * - fetches data for each category and inputs it into categories
 * - create HTML table
 * */

async function setupAndStart() {
  let isLoading = $("#start").text() === "Loading...";

  if (!isLoading) {
    showLoadingView();

    let catIds = await getCategoryIds();

    categories = [];

    for (let catId of catIds) {
      categories.push(await getCategory(catId));
    }

    fillTable();
  }
}

/** On click of start / restart button, set up game. */

$("#start").on("click", setupAndStart);

/** On page load, add event handler for clicking clues */

$(async function() {
  $("#jeopardy").on("click", "td", handleClick);
});