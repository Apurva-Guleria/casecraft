
// ==================================
// CASECRAFT - API CONNECTION
// ==================================

const API_BASE_URL = "http://127.0.0.1:8000";

// Fetch all mystery cases
async function getCases() {
    try {
        const response = await fetch(`${API_BASE_URL}/cases`);

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const cases = await response.json();

        console.log("Cases fetched successfully:", cases);

        return cases;

    } catch (error) {
        console.error("Failed to fetch cases:", error);
        throw error;
    }
}

async function getCaseClues(caseId) {
    try {
        const response = await fetch(
            `${API_BASE_URL}/cases/${caseId}/clues`
        );

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const clues = await response.json();

        console.log("Case clues fetched:", clues);

        return clues;

    } catch (error) {
        console.error("Failed to fetch case clues:", error);
        throw error;
    }
}