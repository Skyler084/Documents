#Which disease has a maximum number of claims.
SELECT disease_name, COUNT(*) as claim_count
FROM projectoutput.claimsdata
GROUP BY disease_name
ORDER BY claim_count DESC
LIMIT 1;


CREATE TABLE projectoutput.DiseaseClaimAnalysis (disease_name VARCHAR(100), max_number_of_claims INT);

#create new table for the answers
INSERT INTO projectoutput.DiseaseClaimAnalysis (disease_name, max_number_of_claims)
SELECT disease_name, COUNT(*) as claim_count
FROM projectoutput.claimsdata
GROUP BY disease_name
ORDER BY claim_count DESC
LIMIT 1;

select * from projectoutput.DiseaseClaimAnalysis