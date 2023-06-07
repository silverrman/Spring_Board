function countdown(num) {
    const intervalId = setInterval(() => {
      if (num === 0) {
        console.log("DONE!");
        clearInterval(intervalId);
      } else {
        console.log(num);
        num--;
      }
    }, 1000);
  }
  