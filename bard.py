from Bard import Chatbot

token ="XAhDGFO_LLKufLdCyreZYocSkTnh0yhV5o4bIxaz-R6v_IqlydL8gqEtJIiJBOST5aWxyw."
chatbot = Chatbot(token)


def prompt_bard(prompt):
    response = chatbot.ask(prompt)
    print(response['content'])


prompt_bard("write code in python for printing fibonacci series")
