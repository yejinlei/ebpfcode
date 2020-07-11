#!/usr/bin/env python
# coding=utf-8

from bcc import BPF

#ebpf program
# 整个eBPF程序都包含在program变量中，这是在
# eBPF虚拟机上的内核中运行的代码
program = '''
/*
 *kprobe__前缀指示bcc工具链将kprobe附加到
 *其后的内核符号上
 *
 */
int kprobe__sys_clone(void *ctx) 
{
    //当调用sys_clone并触发该kprobe时，eBPF程序运行
    //bpf_trace_printk()打印“hello world”到内核的trace buffer(跟踪缓冲区)
    bpf_trace_printk("hello, world!\\n");

    return 0;
}
'''

#python程序的其余部分将eBPF代码加载到内核并运行
b = BPF(text = program) #实例化一个新的BPF对象b
b.trace_print() #BPF_trace_print()对内核的trace buffer(/sys/kerel/debug/tracing/trace_pipe)执行阻塞读取
                # 并将内容打印到标准输出中

#以前将程序编译为eBPF字节码并将其加载到内核的繁琐任务完全是通过实例化一个新的BPF对象来完成的
# 所有的底层工作都在幕后，由python绑定和bcc的libbpf完成
# libbpf是BPF加载器。libbpf在运行时获取之前已经编译好的BPF ELF文件，然后针对运行平台做进一步的处理，并触发BPF程序的加载和验证
