#!/usr/bin/env python
# coding=utf-8

#tracepoint比较稳定，如果可以都建议用tracepoint替代kprobes
#
#可以使用perf list命令来列出可用的tracepoints
#
#将eBPF程序附加到tracepoint上需要内核版本大于4.7

#程序功能：
#           跟踪随机读
from __future__ import print_function
from bcc import BPF

#load eBPF program
b = BPF(text = '''
        /*将eBPF程序附加到tracepoint上*/
        /*  TRACEPOINT_PROBE(random, urandon_read)  \
            是内核的tracepoint random:urandom_read. \
            其格式位于 /sys/kernel/debug/tracing/events/random/urandom_read/format
        */
        TRACEPOINT_PROBE(random, urandom_read) {
                bpf_trace_printk("%d\\n", args->got_bits);

                return 0;
        }
        ''')

#header
print("%-18s %-16s %-6s %s"%("TIME(s)", 
                             "COMM", "PID", "GOTBITS"))

#format output
while 1:
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    print("%-18.9f %-16s %-6d %s"%(ts, task, pid, msg))
