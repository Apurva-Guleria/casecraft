
// ==================================
// CASECRAFT - APPLICATION START
// ==================================

const mainMenu = document.getElementById("main-menu");
const briefingScreen = document.getElementById("briefing-screen");

const caseSelectionScreen = document.getElementById(
    "case-selection-screen"
);

const newGameButton = document.getElementById("new-game-btn");
const caseList = document.getElementById("case-list");

let selectedCaseId = null;
// Function to switch between screens
function showScreen(screen) {

    // Hide all currently active screens
    document.querySelectorAll(".screen").forEach((item) => {
        item.classList.remove("active");
    });

    // Show the requested screen
    screen.classList.add("active");
}


function displayCases(cases) {
    caseList.innerHTML = "";

    cases.forEach((mysteryCase) => {

        const card = document.createElement("div");
        card.classList.add("case-card");

        const title = document.createElement("h2");
        title.textContent = mysteryCase.title;

        const description = document.createElement("p");
        description.textContent = mysteryCase.description;

        const difficulty = document.createElement("span");
        difficulty.classList.add("case-difficulty");
        difficulty.textContent =
            `DIFFICULTY: ${mysteryCase.difficulty}`;

        card.append(title, description, difficulty);

        card.addEventListener("click", () => {

            selectedCaseId = mysteryCase.id;

            console.log("Selected Case ID:", selectedCaseId);

            document.getElementById("case-title").textContent =
                mysteryCase.title;

            document.getElementById("case-description").textContent =
                mysteryCase.description;

            showScreen(briefingScreen);
        });

        caseList.appendChild(card);
    });
}
// New Investigation button interaction

newGameButton.addEventListener("click", async () => {

    try {
        const cases = await getCases();

        if (cases.length === 0) {
            alert("No mystery cases available.");
            return;
        }

        // Show the Case Archive
        displayCases(cases);
        showScreen(caseSelectionScreen);

    } catch (error) {
        alert("Unable to load mystery cases. Please try again.");
        console.error(error);
    }

});


// ==================================
// CRIME SCENE NAVIGATION
// ==================================

const crimeSceneScreen = document.getElementById(
    "crime-scene-screen"
);

const startInvestigationButton = document.getElementById(
    "start-investigation-btn"
);

// Open crime scene when player clicks Begin Investigation
startInvestigationButton.addEventListener("click", async () => {

    try {
        const clues = await getCaseClues(selectedCaseId);
        loadEvidence(clues);

        console.log("Clues for selected case:", clues);

        showScreen(crimeSceneScreen);

    } catch (error) {
        alert("Unable to load clues for this case.");
        console.error(error);
    }

});
