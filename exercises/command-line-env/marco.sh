marco() {
    pwd > /tmp/marco_dir
}

polo() {
    cd "$(cat /tmp/marco_dir)"
}
