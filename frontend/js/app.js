
// ==================================
// CASECRAFT - APPLICATION START
// ==================================

// Get the main menu and briefing screen
const mainMenu = document.getElementById("main-menu");
const briefingScreen = document.getElementById("briefing-screen");

// Get the New Investigation button
const newGameButton = document.getElementById("new-game-btn");

// Function to switch between screens
function showScreen(screen) {

    // Hide all currently active screens
    document.querySelectorAll(".screen").forEach((item) => {
        item.classList.remove("active");
    });

    // Show the requested screen
    screen.classList.add("active");
}

// New Investigation button interaction
newGameButton.addEventListener("click", () => {
    showScreen(briefingScreen);
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

startInvestigationButton.addEventListener("click", () => {
    showScreen(crimeSceneScreen);
});
