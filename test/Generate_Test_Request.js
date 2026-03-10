const { CompactSign, importPKCS8, importX509 } = require('jose');
const crypto = require('crypto');

async function generateTestRequest() {
    // 1. Jouw Self-Signed Certificaat data (DER-encoded string in Base64)
    // In een echte test lees je dit uit je .crt of .pem bestand.
    const certBase64Der = "MIIC..."; // Jouw end-entity certificaat [cite: 359]

    // 2. De Private Key om te signeren (moet passen bij het certificaat)
    const privateKeyPem = `-----BEGIN PRIVATE KEY-----\nMIIEv...`;
    const privateKey = await importPKCS8(privateKeyPem, 'PS256');

    // 3. De Payload (de HTTP body voor het CBS request) [cite: 403-406]
    const payload = JSON.stringify({
        "startdatum": "2026-01-01",
        "einddatum": "2026-30-06",
        "aanleverende_organisatie": "GM0001"
    });

    // 4. Maak de JWS Protected Header [cite: 354-363]
    const encoder = new TextEncoder();
    const sig = await new CompactSign(encoder.encode(payload))
        .setProtectedHeader({
            alg: 'PS256',           // Verplicht algoritme [cite: 355]
            typ: 'JOSE',            // Verplicht type [cite: 356]
            kid: 'test-key-2026',   // Key Identifier [cite: 357]
            x5c: [certBase64Der]    // De certificaatketen [cite: 358]
        })
        .sign(privateKey);

    // 5. Converteer naar "Detached Payload" formaat [cite: 351-352]
    // De standaard output is Header.Payload.Signature.
    // Wij hebben Header..Signature nodig (merk de dubbele punt op).
    const [header, , signature] = sig.split('.');
    const detachedJws = `${header}..${signature}`;

    console.log("--- TEST DATA VOOR JE API ---");
    console.log("Header Name: nlgov-adr-payload-sig");
    console.log("Header Value:", detachedJws);
    console.log("Body:", payload);
}

generateTestRequest();
