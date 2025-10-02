class EmailVilidator:
    def __init__(self, min_length, mails, domains):
        self.min_legth = min_length
        self.mails = mails
        self.domains = domains
    def __validate_name(self, name):
        return len(name) >= self.min_legth

    def __validate_mail(self, mail):
        return mail in self.mails    

    def __validate_domain(self, domain):
        return domain in self.domains
    def validate(self, email):
        if"@" not in email or"."not in email:
            return False
        
        name,rest = email.split("@")
        mail,domain = rest.split(".")

        return self.__validate_name(name) and\
               self.__validate_mail(mail) and\
               self.__validate_domain(domain)

mails = ["gmail","softuni"]
domains = ["com", "bg"]
email_validatetor = EmailVilidator(6, mails, domains)

print(email_validatetor.validate("pe77er@gmail.com"))
print(email_validatetor.validate("georgios@gmail.net"))
print(email_validatetor.validate("stamatito@abv.net"))
print(email_validatetor.validate("abv@softuni.bg"))