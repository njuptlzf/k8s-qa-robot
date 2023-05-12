run_cmd() {
    echo q: $1
    python3 test-flask-client.py $1
    echo ""
}

run_cmd 你好,你是谁 && sleep 10
run_cmd 如何重启 library-web && sleep 10
run_cmd 请重启 && sleep 10
run_cmd 请分析原因