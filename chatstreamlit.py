import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
# Dictionnaire 
responses = {
     "Qu'est-ce que le cancer du sein ?": "Le cancer du sein est une tumeur maligne qui se développe dans les cellules du sein.",
    "Quels sont les symptômes du cancer du sein ?": "Les symptômes du cancer du sein peuvent inclure des bosses, une douleur au sein, des écoulements du mamelon, etc.",
    "Comment diagnostique-t-on le cancer du sein ?": "Le cancer du sein est diagnostiqué par des méthodes telles que la mammographie, l'échographie et la biopsie.",
    "Quels sont les facteurs de risque du cancer du sein ?": "Les facteurs de risque incluent l'âge, les antécédents familiaux, etc.",
    "Comment puis-je prévenir le cancer du sein ?": "La prévention comprend la mammographie régulière et un mode de vie sain.",
    "Quels sont les traitements pour le cancer du sein ?": "Les traitements incluent la chirurgie, la chimiothérapie, la radiothérapie, etc.",
    "Quelle est la survie moyenne pour le cancer du sein ?": "Le taux de survie dépend du stade et du traitement.",
    "Comment puis-je soutenir un proche atteint du cancer du sein ?": "Fournissez un soutien émotionnel et aidez à la gestion des soins médicaux.",
    "Quelles organisations offrent des ressources pour le cancer du sein ?": "Des organisations comme la Ligue contre le cancer sont utiles.",
    "Où puis-je trouver plus d'informations sur le cancer du sein ?": "Consultez des sites Web médicaux fiables et des organisations de lutte contre le cancer.",
    "Est-ce que le cancer du sein est héréditaire ?": "Oui, il peut être lié à des facteurs génétiques.",
    "Quelle est la différence entre une tumeur maligne et une tumeur bénigne ?": "Les tumeurs malignes sont cancéreuses, tandis que les tumeurs bénignes ne le sont pas.",
    "Le cancer du sein est-il fréquent ?": "Oui, il est fréquent chez les femmes, mais peut également affecter les hommes.",
    "Quels sont les types de cancer du sein ?": "Il existe différents types, y compris le carcinome canalaire et le carcinome lobulaire.",
    "Quand devrais-je consulter un médecin en cas de doute ?": "Consultez un médecin si vous remarquez des symptômes inquiétants.",
    "Quelles sont les étapes du traitement du cancer du sein ?": "Le traitement comprend le diagnostic, la chirurgie, la chimiothérapie, la radiothérapie, la surveillance, etc.",
    "Puis-je prévenir le cancer du sein par le régime alimentaire ?": "Un régime alimentaire sain peut aider, mais il ne garantit pas la prévention.",
    "Comment se passe la mammographie ?": "La mammographie est une radiographie du sein qui peut détecter les anomalies.",
    "Quels sont les symptômes du cancer du sein avancé ?": "Les symptômes avancés peuvent inclure des douleurs osseuses, des difficultés respiratoires, etc.",
    "Y a-t-il des groupes de soutien pour les patients atteints du cancer du sein ?": "Oui, de nombreux groupes de soutien existent pour les patients et leurs familles.",
    "Quelle est la différence entre une tumeur maligne et une tumeur bénigne ?": "Une tumeur maligne est cancéreuse et peut se propager, tandis qu'une tumeur bénigne n'est pas cancéreuse et ne se propage pas.",
    "Le cancer du sein peut-il toucher les hommes ?": "Oui, bien que le cancer du sein soit moins fréquent chez les hommes, il peut les affecter.",
    "Quelles sont les étapes du traitement par chimiothérapie ?": "Le traitement par chimiothérapie comprend plusieurs étapes, notamment l'évaluation, la planification, l'administration de médicaments, et la surveillance des effets secondaires.",
    "Quelles sont les méthodes de prévention du cancer du sein ?": "La prévention du cancer du sein implique des contrôles réguliers, un mode de vie sain, l'auto-examen des seins et la réduction des facteurs de risque.",
    "Quels sont les symptômes du cancer du sein avancé ?": "Les symptômes du cancer du sein avancé peuvent inclure des douleurs osseuses, des difficultés respiratoires, une perte de poids non expliquée et des changements cutanés.",
    "Y a-t-il des groupes de soutien pour les patients atteints du cancer du sein ?": "Oui, de nombreux groupes de soutien existent pour les patients et leurs familles. Ils offrent un soutien émotionnel, des informations utiles et un espace pour partager des expériences.",
    "Comment le cancer du sein est-il lié à l'exposition aux radiations ?": "Une exposition prolongée aux radiations, en particulier pendant l'enfance, peut augmenter le risque de développer un cancer du sein.",
    "Comment le cancer du sein est-il diagnostiqué chez les femmes transgenres ?": "Le diagnostic du cancer du sein chez les femmes transgenres repose sur l'auto-examen des seins, la mammographie et d'autres méthodes de dépistage similaires à celles des femmes cisgenres.",
    "Quels sont les effets du tabagisme sur le cancer du sein ?": "Le tabagisme peut augmenter le risque de cancer du sein, en particulier chez les femmes prédisposées génétiquement. Il est donc recommandé d'éviter le tabac.",
    "Comment la psychothérapie peut-elle aider les patients atteints du cancer du sein ?": "La psychothérapie peut offrir un soutien émotionnel, aider à faire face à l'anxiété et à la dépression, et améliorer la qualité de vie des patients atteints du cancer du sein.",
    "Quels sont les avantages de la thérapie génique dans le traitement du cancer du sein ?": "La thérapie génique est une approche prometteuse en développement pour cibler spécifiquement les cellules cancéreuses du sein, offrant ainsi un traitement plus précis et moins invasif.",
    "Comment le cancer du sein est-il lié à la thérapie de remplacement hormonale ?": "L'utilisation à long terme de la thérapie de remplacement hormonale, en particulier avec des hormones combinées, peut augmenter le risque de cancer du sein. Il est essentiel de discuter des avantages et des risques avec un professionnel de la santé.",
    "Comment le cancer du sein est-il diagnostiqué chez les femmes ménopausées ?": "Les femmes ménopausées peuvent toujours bénéficier de la mammographie et de l'auto-examen des seins pour le dépistage du cancer du sein.",
    "Comment le système immunitaire peut-il jouer un rôle dans la lutte contre le cancer du sein ?": "L'immunothérapie est une approche émergente qui stimule le système immunitaire pour cibler et combattre les cellules cancéreuses du sein, offrant de nouveaux espoirs de traitement."
}

basic_responses = {
     "Bonjour": "Bonjour ! Comment puis-je vous aider avec des informations sur le cancer du sein aujourd'hui ?",
    "t qui  ?": "Je suis juste un chatbot, mais je suis là pour vous aider avec toutes les questions que vous avez sur le cancer du sein !",
    "votre nom ": "Je n'ai pas de nom, mais vous pouvez m'appeler le Chatbot du Cancer du Sein."
}

def chatbot_response(user_question):
    user_question = user_question.lower()  
    words = word_tokenize(user_question)  
    words = [word for word in words if word not in stopwords.words('french')]  # Mots vides en français
    
    matched_responses = []
    for question, response in responses.items():
        if all(word in question.lower() for word in words):
            matched_responses.append(response)

    if matched_responses:
        return matched_responses
    else:
        return "Je suis désolé, je ne comprends pas votre question. Je réponds uniquement aux questions concernant le cancer du sein."

# Interface
st.title("Chatbot sur le Cancer du Sein")
user_question = st.text_input("Posez une question sur le cancer du sein (ou tapez 'exit' pour quitter) :")

if user_question:
    if user_question in basic_responses:
        st.text(basic_responses[user_question])
    else:
        response = chatbot_response(user_question)
        if isinstance(response, list):
            st.text("Possibles Réponses du Chatbot :")
            for r in response:
                st.text("- " + r)
        else:
            st.text("Réponse du Chatbot : " + response)

if st.button("Quitter"):
    st.stop()
