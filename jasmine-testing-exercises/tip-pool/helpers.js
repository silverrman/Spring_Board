
// accepts 'tipAmt', 'billAmt', 'tipPercent' and sums total from allPayments objects
function sumPaymentTotal(type) {
  let total = 0;

  for (let key in allPayments) {
    let payment = allPayments[key];

    total += Number(payment[type]);
  }

  return total;
}

// converts the bill and tip amount into a tip percent
function calculateTipPercent(billAmt, tipAmt) {
  return Math.round(100 / (billAmt / tipAmt));
}

// expects a table row element, appends a newly created td element from the value
function appendTd(tr, value) {
  let newTd = document.createElement('td');
  newTd.innerText = value;
  tr.append(newTd);
}

// expects a table row element, appends a td with 'X' that removes the row on click
function appendDeleteBtn(tr) {
  const td = document.createElement('td');
  td.innerText = 'X';
  td.className = 'deleteBtn';
  td.style.cursor = 'pointer';
  td.addEventListener('click', function(evt) {
    tr.remove();
  });
  tr.append(td);
}
