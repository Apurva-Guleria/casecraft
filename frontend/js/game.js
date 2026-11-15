
// ==================================
// CASECRAFT - DYNAMIC EVIDENCE SYSTEM
// ==================================

const evidenceHotspotsContainer = document.getElementById(
    "evidence-hotspots"
);

const discoveredCluesContainer = document.getElementById(
    "discovered-clues"
);

const clueCount = document.getElementById("clue-count");

// Store discovered evidence IDs
const discoveredEvidence = new Set();

// Load clues for the selected case
function loadEvidence(clues) {

    // Clear previous case evidence
    evidenceHotspotsContainer.innerHTML = "";
    discoveredCluesContainer.innerHTML = "";
    discoveredEvidence.clear();

    // Update total clue counter
    clueCount.textContent = `0 / ${clues.length}`;

    clues.forEach((clue, index) => {

        // Create hotspot
        const hotspot = document.createElement("button");

        hotspot.classList.add("evidence-hotspot");

        hotspot.dataset.clue = clue.id;
        hotspot.title = `Investigate ${clue.title}`;
        hotspot.setAttribute(
            "aria-label",
            `Investigate ${clue.title}`
        );

        hotspot.innerHTML = "<span>?</span>";

        // Handle evidence discovery
        hotspot.addEventListener("click", () => {

            if (discoveredEvidence.has(clue.id)) {
                return;
            }

            discoveredEvidence.add(clue.id);

            // Create evidence card
            const clueCard = document.createElement("div");

            clueCard.classList.add("clue-card");

            const title = document.createElement("h3");
            title.textContent = clue.title;

            const description = document.createElement("p");
            description.textContent = clue.description;

            clueCard.append(title, description);

            discoveredCluesContainer.appendChild(clueCard);

            // Update counter
            clueCount.textContent =
                `${discoveredEvidence.size} / ${clues.length}`;

            // Mark hotspot discovered
            hotspot.classList.add("discovered");

            console.log("Evidence collected:", clue.title);

            showEvidenceNotification(clue.title);

        });

        evidenceHotspotsContainer.appendChild(hotspot);

    });

    console.log("Evidence hotspots generated:", clues.length);
}


// ==================================
// EVIDENCE DISCOVERY NOTIFICATION
// ==================================

function showEvidenceNotification(title) {

    let notification = document.getElementById(
        "evidence-notification"
    );

    if (!notification) {

        notification = document.createElement("div");

        notification.id = "evidence-notification";

        document.body.appendChild(notification);
    }

    notification.innerHTML = `
        <span>NEW EVIDENCE DISCOVERED</span>
        <h3>${title}</h3>
    `;

    notification.classList.remove("show");

    // Restart animation
    void notification.offsetWidth;

    notification.classList.add("show");

    setTimeout(() => {
        notification.classList.remove("show");
    }, 2500);
}
