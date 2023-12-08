import tkinter as tk
from tkinter import ttk, messagebox

class VoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voting System")
        self.root.geometry("500x300")

        self.john_votes = 0
        self.jane_votes = 0
        self.democrat_votes = 0
        self.republican_votes = 0
        self.voted_ids = set()

        self.create_widgets()

    def create_widgets(self):
        self.vote_label = tk.Label(self.root, text="VOTE MENU")
        self.vote_label.pack()

        self.id_entry_label = tk.Label(self.root, text="Enter your ID:")
        self.id_entry_label.pack()

        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.party_tab = tk.Frame(self.notebook)
        self.candidate_tab = tk.Frame(self.notebook)

        self.notebook.add(self.party_tab, text="Select Party")
        self.notebook.add(self.candidate_tab, text="Select Candidate")

        self.create_party_tab()
        self.create_candidate_tab()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        # Labels to display current vote counts
        self.vote_tracker_label = tk.Label(self.root, text="Votes: John - 0 Jane - 0")
        self.vote_tracker_label.pack()

        self.democrat_label = tk.Label(self.root, text="Democrat Votes: 0")
        self.democrat_label.pack()

        self.republican_label = tk.Label(self.root, text="Republican Votes: 0")
        self.republican_label.pack()

    def create_party_tab(self):
        party_label = tk.Label(self.party_tab, text="Select a party:")
        party_label.pack()

        democrat_button = tk.Button(self.party_tab, text="Vote for Democrat",
                                    command=lambda: self.switch_to_candidate_tab(3))
        democrat_button.pack()

        republican_button = tk.Button(self.party_tab, text="Vote for Republican",
                                      command=lambda: self.switch_to_candidate_tab(4))
        republican_button.pack()

    def create_candidate_tab(self):
        candidate_label = tk.Label(self.candidate_tab, text="Select a candidate:")
        candidate_label.pack()

        john_button = tk.Button(self.candidate_tab, text="Vote for John",
                                command=lambda: self.vote_for_candidate(1))
        john_button.pack()

        jane_button = tk.Button(self.candidate_tab, text="Vote for Jane",
                                command=lambda: self.vote_for_candidate(2))
        jane_button.pack()

    def switch_to_candidate_tab(self, party_option):
        self.selected_party_option = party_option
        self.notebook.select(self.candidate_tab)

    def vote_for_candidate(self, candidate_option):
        vote_id = self.id_entry.get()

        if not vote_id:
            messagebox.showinfo("Error", "Please enter your ID.")
        elif vote_id in self.voted_ids:
            messagebox.showinfo("Error", "You have already voted.")
        else:
            if self.selected_party_option == 3:
                self.democrat_votes += 1
            elif self.selected_party_option == 4:
                self.republican_votes += 1

            if candidate_option == 1:
                self.john_votes += 1
            elif candidate_option == 2:
                self.jane_votes += 1

            self.voted_ids.add(vote_id)
            self.update_vote_tracker()
            self.notebook.select(self.party_tab)
            self.id_entry.delete(0, tk.END)

    def update_vote_tracker(self):
        tracker_text = f"Votes: John - {self.john_votes}, Jane - {self.jane_votes}"
        self.vote_tracker_label.config(text=tracker_text)

        democrat_text = f"Democrat Votes: {self.democrat_votes}"
        republican_text = f"Republican Votes: {self.republican_votes}"
        self.democrat_label.config(text=democrat_text)
        self.republican_label.config(text=republican_text)

    def run(self):
        self.root.mainloop()

    def display_results(self):
        total_votes = self.john_votes + self.jane_votes + self.democrat_votes + self.republican_votes
        result_text = (
            f"John: {self.john_votes}\n"
            f"Jane: {self.jane_votes}\n"
            f"Democrat: {self.democrat_votes}\n"
            f"Republican: {self.republican_votes}\n"
            f"Total Votes: {total_votes}"
        )
        messagebox.showinfo("Results", result_text)

if __name__ == "__main__":
    app = VoteApp()
    app.run()
