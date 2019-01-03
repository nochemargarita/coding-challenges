import unittest


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        recipients = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.find('+')]
            recipients.add(local.replace('.', '') + '@' + domain)
        return len(recipients)


class Test(unittest.TestCase):

    def test_numUniqueEmails_1(self):
        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"]
        actual = Solution().numUniqueEmails(emails)
        expected = 2

        self.assertEqual(actual, expected)

    def test_numUniqueEmails_2(self):
        emails = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com",
        "fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com",
        "fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com",
        "fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com",
        "r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com",
        "r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com",
        "r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com",
        "fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com",
        "fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
        actual = Solution().numUniqueEmails(emails)
        expected = 2

        self.assertEqual(actual, expected)

    def test_numUniqueEmails_3(self):
        emails = ['a@y.com', 'a+a.a@y.com']
        actual = Solution().numUniqueEmails(emails)
        expected = 1

        self.assertEqual(actual, expected)

unittest.main(verbosity=2)