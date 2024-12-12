class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()  # Use a set to store unique email addresses
        for email in emails:
            local, domain = email.split('@')  # Split into local and domain parts
            
            # Process the local part: Remove dots and ignore everything after '+'
            local = local.split('+')[0].replace('.', '')  # Remove '.' and ignore after '+'
            
            # Combine the cleaned local and domain parts
            result = local + '@' + domain
            
            # Add the cleaned email to the set
            res.add(result)
        
        # Return the count of unique emails
        return len(res)