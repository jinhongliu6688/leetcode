const updateUserProfile = (firstName, lastName) => {
    // TODO
    fetch("https://api.learnjavascript.online/demo/user.json", {
        method: "PUT",
        body: JSON.stringify({
            firstName: firstName, 
            lastName: lastName
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error(error)
    })

}

// Sample usage - do not modify
const form = document.querySelector("#user-form");
const fName = document.querySelector("#first-name");
const lName = document.querySelector("#last-name");

form.addEventListener("submit", event => {
    event.preventDefault();

    updateUserProfile(fName.value, lName.value);
});
