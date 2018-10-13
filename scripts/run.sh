DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
digest generate --component MONKEYUSER --component XKCD - | $DIR/send.sh "${1:-$(git config --get user.email)}"
