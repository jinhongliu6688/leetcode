const saveGrade = grade => {
    // TODO
    fetch("https://api.learnjavascript.online/demo/grades.json", {
        method: "POST",
        body: JSON.stringify({
            grade: grade
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error(error)
    })
};

// Sample usage - do not modify
const form = document.querySelector("#grades-form");
const userGrade = document.querySelector("#user-grade");

form.addEventListener("submit", event => {
    event.preventDefault();

    saveGrade(userGrade.value);
});
