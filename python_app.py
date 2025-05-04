# collect email from user
# split the email using the @ , the first part is the user name , the second part is gonna be saved as domain
# spilt domain using .,
#Example:
#hallo

#codewithtomi.com 

def main():
    print("welcome to the email slicer app")
    print("")

    email_input = input("input your email address: ")

    (username,domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
     
    print("Username: " , username)
    print("Domain: " , domain)
    print("Extension: " , extension)

while True:
  main()    