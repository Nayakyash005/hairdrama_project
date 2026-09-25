class GmailService:
    def __init__(self):
        self.sender = "noreply@example.com"

    def send_welcome_email(self, email: str, full_name: str = "User") -> str:
        # Replace this with actual Gmail SMTP or API logic later
        print(f"Sending welcome email to {email} for {full_name}")
        return "Email sent successfully"

    def send_task_update_email(self, email: str, task_title: str) -> str:
        print(f"Sending task update email to {email} for task: {task_title}")
        return "Task email sent successfully"
