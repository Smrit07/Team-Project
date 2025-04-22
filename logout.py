class SessionManager:
    def __init__(self):
        self.active_user = None

    def login(self, username):
        if username:
            self.active_user = username
            print(f"[INFO] {username} logged in successfully.")
        else:
            print("[ERROR] Username cannot be empty.")

    def logout(self):
        if self.active_user:
            print(f"[INFO] {self.active_user} logge2d out successfully.")
            self.active_user = None
        else:
            print("[WARNING] No active session to logout from.")

    def is_logged_in(self):
        return self.active_user is not None

def main():
    session = SessionManager()

    while True:
        print("\nOptions:\n1. Login\n2. Logout\n3. Check Session\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            username = input("Enter username: ").strip()
            session.login(username)
        elif choice == '2':
            session.logout()
        elif choice == '3':
            if session.is_logged_in():
                print(f"[SESSION ACTIVE] Logged in as {session.active_user}.")
            else:
                print("[SESSION INACTIVE] No user logged in.")
        elif choice == '4':
            print("Exiting application...")
            break
        else:
            print("[ERROR] Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()