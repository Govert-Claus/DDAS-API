const { compactVerify, importX509 } = require('jose');

// Haal eerst de header (incomingHeader) en de body (rawBody) uit het bericht en voer dan onderstaande functie uit

async function validateRequest(incomingHeader, rawBody) {
    try {
        // 1. Splits de detached header [cite: 351-352]
        // De header ziet eruit als: Header..Signature
        const [headerB64, , signatureB64] = incomingHeader.split('.');

        if (!headerB64 || !signatureB64) {
            throw new Error("Ongeldig handtekeningformaat");
        }

        // 2. Decodeer de header om het certificaat te vinden [cite: 371-372]
        const header = JSON.parse(Buffer.from(headerB64, 'base64url').toString());

        // Controleer of het juiste algoritme is gebruikt [cite: 342, 355]
        if (header.alg !== 'PS256') {
            throw new Error("Onjuist algoritme: DDAS vereist PS256");
        }

        // 3. Haal het certificaat uit de x5c header [cite: 346, 358-359]
        const certChain = header.x5c;
        if (!certChain || certChain.length === 0) {
            throw new Error("Geen certificaat (x5c) gevonden in de header");
        }

        // Het eerste certificaat is het 'end-entity' certificaat van de verzender
        const senderCertPem = `-----BEGIN CERTIFICATE-----\n${certChain[0]}\n-----END CERTIFICATE-----`;
        const publicKey = await importX509(senderCertPem, 'PS256');

        // 4. Construeer het volledige JWS bericht voor verificatie
        // We voegen de body weer toe tussen de twee punten (Base64URL encoded)
        const bodyB64 = Buffer.from(rawBody).toString('base64url');
        const fullJws = `${headerB64}.${bodyB64}.${signatureB64}`;

        // 5. Verifieer de handtekening [cite: 377]
        const { protectedHeader } = await compactVerify(fullJws, publicKey);

        console.log("✅ Validatie geslaagd!");
        console.log("Bericht is afkomstig van (KID):", protectedHeader.kid);
        return true;

    } catch (error) {
        console.error("❌ Validatie gefaald:", error.message);
        return false;
    }
}

// TEST RUN:
// validateRequest("eyJhbGciOiJQUzI1NiIs...", '{"startdatum":"2026-01-01",...}');
