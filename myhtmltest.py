#! /usr/bin/python
#
from myhtml import *

print Html("test",
   Form("zzz.html",#CheckBox("manual", True),
#        NL(),
#        TextBox("test","111"),
#        NL(),
#        SubmitButton("save"),
#        CancelButton("cancel"),
#        NL(),
#        HyperLink("google.com"),
#        BR(),
        Table("","xxx"
        #   TR(TH("1"),TH("2"),TH("3")),
        #    TR(TD("test"),TD("zzz"),TD("aaa")),
        #    TR(TD(Input("test")),TD("MY"),TD("ny"))
           ),
        BR(),
        Table("border = 1",
           TR(TH("1"),TH("2"),TH("3")),
            TR(TD("4"),TD("5"),TD("6")),
            TR(TD("7"),TD("8"),TD("9"))
           ),
        BR(),
#        Header("zzzz"),
        Paragraph("asd asdf wer qwer qwerty"),
       )
   )
