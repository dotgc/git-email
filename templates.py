#!/usr/bin/env python

REF_CREATED_SUBJECT_TEMPLATE = (
    '%(emailprefix)s%(refname_type)s %(short_refname)s created'
    ' (now %(newrev_short)s)'
)
REF_UPDATED_SUBJECT_TEMPLATE = (
    '%(emailprefix)s%(refname_type)s %(short_refname)s updated'
    ' (%(oldrev_short)s -> %(newrev_short)s)'
)
REF_DELETED_SUBJECT_TEMPLATE = (
    '%(emailprefix)s%(refname_type)s %(short_refname)s deleted'
    ' (was %(oldrev_short)s)'
)

COMBINED_REFCHANGE_REVISION_SUBJECT_TEMPLATE = (
    '%(emailprefix)s%(refname_type)s %(short_refname)s updated: %(oneline)s'
)

REFCHANGE_HEADER_TEMPLATE = """\
Date: %(send_date)s
To: %(recipients)s
Subject: %(subject)s
MIME-Version: 1.0
Content-Type: text/%(contenttype)s; charset=%(charset)s
Content-Transfer-Encoding: 8bit
Message-ID: %(msgid)s
From: %(fromaddr)s
Reply-To: %(reply_to)s
X-Git-Host: %(fqdn)s
X-Git-Repo: %(repo_shortname)s
X-Git-Refname: %(refname)s
X-Git-Reftype: %(refname_type)s
X-Git-Oldrev: %(oldrev)s
X-Git-Newrev: %(newrev)s
X-Git-NotificationType: ref_changed
X-Git-Multimail-Version: %(multimail_version)s
Auto-Submitted: auto-generated
"""

REFCHANGE_INTRO_TEMPLATE = """\
This is an automated email from the git hooks/post-receive script.

%(pusher)s pushed a change to %(refname_type)s %(short_refname)s
in repository %(repo_shortname)s.

"""


FOOTER_TEMPLATE = """\

-- \n\
To stop receiving notification emails like this one, please contact
%(administrator)s.
"""


REWIND_ONLY_TEMPLATE = """\
This update removed existing revisions from the reference, leaving the
reference pointing at a previous point in the repository history.

 * -- * -- N   %(refname)s (%(newrev_short)s)
            \\
             O -- O -- O   (%(oldrev_short)s)

Any revisions marked "omit" are not gone; other references still
refer to them.  Any revisions marked "discard" are gone forever.
"""


NON_FF_TEMPLATE = """\
This update added new revisions after undoing existing revisions.
That is to say, some revisions that were in the old version of the
%(refname_type)s are not in the new version.  This situation occurs
when a user --force pushes a change and generates a repository
containing something like this:

 * -- * -- B -- O -- O -- O   (%(oldrev_short)s)
            \\
             N -- N -- N   %(refname)s (%(newrev_short)s)

You should already have received notification emails for all of the O
revisions, and so the following emails describe only the N revisions
from the common base, B.

Any revisions marked "omit" are not gone; other references still
refer to them.  Any revisions marked "discard" are gone forever.
"""


NO_NEW_REVISIONS_TEMPLATE = """\
No new revisions were added by this update.
"""


DISCARDED_REVISIONS_TEMPLATE = """\
This change permanently discards the following revisions:
"""


NO_DISCARDED_REVISIONS_TEMPLATE = """\
The revisions that were on this %(refname_type)s are still contained in
other references; therefore, this change does not discard any commits
from the repository.
"""


NEW_REVISIONS_TEMPLATE = """\
The %(tot)s revisions listed above as "new" are entirely new to this
repository and will be described in separate emails.  The revisions
listed as "add" were already present in the repository and have only
been added to this reference.

"""


TAG_CREATED_TEMPLATE = """\
      at %(newrev_short)-8s (%(newrev_type)s)
"""


TAG_UPDATED_TEMPLATE = """\
*** WARNING: tag %(short_refname)s was modified! ***

    from %(oldrev_short)-8s (%(oldrev_type)s)
      to %(newrev_short)-8s (%(newrev_type)s)
"""


TAG_DELETED_TEMPLATE = """\
*** WARNING: tag %(short_refname)s was deleted! ***

"""


# The template used in summary tables.  It looks best if this uses the
# same alignment as TAG_CREATED_TEMPLATE and TAG_UPDATED_TEMPLATE.
BRIEF_SUMMARY_TEMPLATE = """\
%(action)8s %(rev_short)-8s %(text)s
"""


NON_COMMIT_UPDATE_TEMPLATE = """\
This is an unusual reference change because the reference did not
refer to a commit either before or after the change.  We do not know
how to provide full information about this reference change.
"""


REVISION_HEADER_TEMPLATE = """\
Date: %(send_date)s
To: %(recipients)s
Cc: %(cc_recipients)s
Subject: %(emailprefix)s%(num)02d/%(tot)02d: %(oneline)s
MIME-Version: 1.0
Content-Type: text/%(contenttype)s; charset=%(charset)s
Content-Transfer-Encoding: 8bit
From: %(fromaddr)s
Reply-To: %(reply_to)s
In-Reply-To: %(reply_to_msgid)s
References: %(reply_to_msgid)s
X-Git-Host: %(fqdn)s
X-Git-Repo: %(repo_shortname)s
X-Git-Refname: %(refname)s
X-Git-Reftype: %(refname_type)s
X-Git-Rev: %(rev)s
X-Git-NotificationType: diff
X-Git-Multimail-Version: %(multimail_version)s
Auto-Submitted: auto-generated
"""

REVISION_INTRO_TEMPLATE = """\
This is an automated email from the git hooks/post-receive script.

%(pusher)s pushed a commit to %(refname_type)s %(short_refname)s
in repository %(repo_shortname)s.

"""

LINK_TEXT_TEMPLATE = """\
View the commit online:
%(browse_url)s

"""

LINK_HTML_TEMPLATE = """\
<p><a href="%(browse_url)s">View the commit online</a>.</p>
"""


REVISION_FOOTER_TEMPLATE = FOOTER_TEMPLATE


# Combined, meaning refchange+revision email (for single-commit additions)
COMBINED_HEADER_TEMPLATE = """\
Date: %(send_date)s
To: %(recipients)s
Subject: %(subject)s
MIME-Version: 1.0
Content-Type: text/%(contenttype)s; charset=%(charset)s
Content-Transfer-Encoding: 8bit
Message-ID: %(msgid)s
From: %(fromaddr)s
Reply-To: %(reply_to)s
X-Git-Host: %(fqdn)s
X-Git-Repo: %(repo_shortname)s
X-Git-Refname: %(refname)s
X-Git-Reftype: %(refname_type)s
X-Git-Oldrev: %(oldrev)s
X-Git-Newrev: %(newrev)s
X-Git-Rev: %(rev)s
X-Git-NotificationType: ref_changed_plus_diff
X-Git-Multimail-Version: %(multimail_version)s
Auto-Submitted: auto-generated
"""

COMBINED_INTRO_TEMPLATE = """\
This is an automated email from the git hooks/post-receive script.

%(pusher)s pushed a commit to %(refname_type)s %(short_refname)s
in repository %(repo_shortname)s.

"""

COMBINED_FOOTER_TEMPLATE = FOOTER_TEMPLATE

