#!/usr/bin/env python
# coding=utf-8

from bcc import BPF

b = BPF(text = '''
        BPF_HASH(callers, u64, unsigned long);

        /*TRACEPOINT_PROBE()的参数是跟踪点的类别和事件本身  \
         * 跟踪点的类别在/sys/kernel/debug/tracing/events文件夹下   \
         * vmscan是events里的一个类别，mm_vmscan_writepage()是vmscan/里的事件   \
         * TRACEPOINT_PROBE()会将跟踪点的类别和事件直接转换为debugfs文件系统的层次结构布局
         */
        TRACEPOINT_PROBE(vmscan, mm_vmscan_writepage) {
                //bpf_trace_printk("hello world\\n");

                return 0;
        }
        ''')

b.trace_print()
