function transitionAfterPageLoad() {
    document.getElementById("body").classList.remove("no-transition");
}

// call the function inside an Immediately Invoked Function Expression (IIFE) to invoke it immediately after page load
(function () {
    transitionAfterPageLoad();
})();

window.addEventListener("DOMContentLoaded", function () {
    document.querySelector("#body").classList.remove("no-transition");
});
