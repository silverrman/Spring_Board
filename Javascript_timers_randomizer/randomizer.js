function randomGame() {
    let tries = 0;
    
    while (Math.random() <= 0.75) {
      tries++;
    }
    
    console.log(`it took ${tries} try/tries.`);
  }
  