import sys

def run_quiz():
    questions = [
        {
            "vraag": "Je hebt een nieuw bestand gemaakt. Welk commando gebruik je om het klaar te zetten voor een commit?",
            "opties": ["A. git commit", "B. git push", "C. git add", "D. git status"],
            "antwoord": "C"
        },
        {
            "vraag": "Wat is het nut van 'git pull'?",
            "opties": [
                "A. Je eigen code naar GitHub sturen", 
                "B. De nieuwste wijzigingen van je vriend binnenhalen", 
                "C. Een nieuw bestand aanmaken", 
                "D. Je computer afsluiten"
            ],
            "antwoord": "B"
        },
        {
            "vraag": "Waarom is OneDrive soms een vijand van Git?",
            "opties": [
                "A. Omdat OneDrive te traag is", 
                "B. Omdat ze allebei tegelijk bestanden proberen te synchroniseren/vergrendelen", 
                "C. Omdat Git geen internet nodig heeft", 
                "D. Omdat Python niet werkt op OneDrive"
            ],
            "antwoord": "B"
        },
        {
            "vraag": "Wat doet het commando 'git status'?",
            "opties": [
                "A. Het verwijdert al je fouten", 
                "B. Het stuurt je code naar de docent", 
                "C. Het laat zien welke bestanden zijn aangepast of nog niet gevolgd worden", 
                "D. Het installeert de nieuwste versie van Python"
            ],
            "antwoord": "C"
        }
    ]

    score = 0
    print("--- 🚀 DE GROTE GIT & GITHUB QUIZ 🚀 ---")
    print("Beantwoord de vragen met A, B, C of D\n")

    for i, q in enumerate(questions):
        print(f"Vraag {i+1}: {q['vraag']}")
        for optie in q['opties']:
            print(optie)
        
        keuze = input("Jouw antwoord: ").strip().upper()

        if keuze == q['antwoord']:
            print("✅ Helemaal juist!\n")
            score += 1
        else:
            print(f"❌ Helaas, het juiste antwoord was {q['antwoord']}.\n")

    print(f"--- QUIZ KLAAR ---")
    print(f"Je score: {score}/{len(questions)}")
    
    if score == len(questions):
        print("Status: Git-Legende! Je bent klaar voor de samenwerking. 😎")
    elif score >= 2:
        print("Status: Je bent op de goede weg, maar blijf oefenen met je copain. 👍")
    else:
        print("Status: Oei, lees de tips hierboven nog eens goed door! 📚")

if __name__ == "__main__":
    run_quiz()
