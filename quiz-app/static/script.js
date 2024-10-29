window.onload = function() {
    let time = 60;  // 60 seconds timer
    const timerDiv = document.getElementById('timer');
    
    const interval = setInterval(function() {
        time--;
        timerDiv.innerHTML = `Time left: ${time} seconds`;
        
        if (time <= 0) {
            clearInterval(interval);
            document.forms[0].submit();  // To auto-submit form
        }
    }, 1000);
};
