#!/bin/bash

mutt \
  -e "set content_type=text/html"\
  -e "set from = \"$1\""\
  -e "set realname = \"David Buckley\""\
  -e "set imap_user = \"$1\""\
  -e "set imap_pass = \"${APP_PASSWORD}\""\
  -e "set folder = \"imaps://imap.gmail.com:993\""\
  -e "set spoolfile = \"+INBOX\""\
  -e "set postponed = \"+[Gmail]/Drafts\""\
  -e "set header_cache =~/.mutt/cache/headers"\
  -e "set message_cachedir =~/.mutt/cache/bodies"\
  -e "set certificate_file =~/.mutt/certificates"\
  -e "set smtp_url = \"smtp://buckley.w.david@smtp.gmail.com:587/\""\
  -e "set smtp_pass = \"${APP_PASSWORD}\""\
  -e "set record = \"\""\
  -e "set move = no "\
  -e "set imap_keepalive = 900" \
  -s "test" "$1" < ${2:-/dev/stdin}
