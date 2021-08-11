def username_generator(first_name, last_name):
      username = first_name[:3] + last_name[:4]
      return username

def password_generator(user_name):
      password = ""
      for i in range(0, len(user_name)):
            password += user_name[i-1]
      return password
