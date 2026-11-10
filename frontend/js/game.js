
// ==================================
// CASECRAFT - EVIDENCE INTERACTION
// ==================================

const evidenceHotspots = document.querySelectorAll(
    ".evidence-hotspot"
);

const discoveredCluesContainer = document.getElementById(
    "discovered-clues"
);

const clueCount = document.getElementById("clue-count");

// Evidence information
const evidenceData = {
    "diamond-case": {
        title: "Empty Diamond Case",
        description: "The diamond is missing, but the display case shows no obvious signs of forced entry."
    },

    "broken-glass": {
        title: "Broken Glass",
        description: "Several glass fragments lie scattered across the floor. Some pieces appear freshly broken."
    },

    "overturned-chair": {
        title: "Overturned Chair",
        description: "A chair has been knocked over. It may indicate a struggle or a hurried escape."
    }
};

// Store discovered evidence
const discoveredEvidence = new Set();

// Handle evidence clicks
evidenceHotspots.forEach((hotspot) => {

    hotspot.addEventListener("click", () => {

        const clueId = hotspot.dataset.clue;

        // Prevent duplicate discoveries
        if (discoveredEvidence.has(clueId)) {
            return;
        }

        const evidence = evidenceData[clueId];

        if (!evidence) return;

        discoveredEvidence.add(clueId);

        // Display discovered evidence
        const clueCard = document.createElement("div");

        clueCard.classList.add("clue-card");

        clueCard.innerHTML = `
            <h3>${evidence.title}</h3>
            <p>${evidence.description}</p>
        `;

        discoveredCluesContainer.appendChild(clueCard);

        // Update evidence counter
        clueCount.textContent = discoveredEvidence.size;

        // Mark hotspot as discovered
        hotspot.classList.add("discovered");

        console.log("Evidence collected:", evidence.title);

        // Show evidence discovery notification
        showEvidenceNotification(evidence.title);

    });

});
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