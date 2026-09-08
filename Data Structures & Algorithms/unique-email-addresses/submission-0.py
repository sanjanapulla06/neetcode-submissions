class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for i in range(len(emails)):
            email = emails[i]
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)