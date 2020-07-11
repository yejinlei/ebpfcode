#!/usr/bin/env python
# coding=utf-8

from bcc import BPF

program = '''
int kprobe__sys_clone(void *ctx)
{
    bpf_trace_printk("hello, world!\\n");

    return 0;
}
'''

b = BPF(text = program)
b.trace_print()
