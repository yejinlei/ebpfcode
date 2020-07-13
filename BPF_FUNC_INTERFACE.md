#### BPF接口函数

| 函数                       | 功能                                                         |
| :------------------------- | :----------------------------------------------------------- |
| bpf_ktime_get_ns()         | 返回纳秒时间                                                 |
| BPF_HASH(last)             | 创建BPF映射对象，叫做last。如果没有指定任何参数，所以健值都是无符号64位 |
| bpf_trace_printk()         | 输出字符串，类似printf ,在调试中使用个，工具中使用BPF_PERF_OUTPUT() |
| bpf_get_current_pid_tgid() | 函数获得pid进程,其中低32位是进程ID,高32位是组id              |
| BPF_PERF_OUTPUT(events)    | 命名输出频道名字为events.                                    |
| bpf_get_current_common()   | 函数用当前进程名字填充第一个参数地址                         |
| events.perf_submit()       | 通过ring buffer将事件提交到用户层                            |

