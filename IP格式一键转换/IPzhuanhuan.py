import os

def start_process():
    # --- 按照你的要求重新命名文件名 ---
    input_file = 'in_ip.txt'
    output_file = 'out_ip.txt'
    # -------------------------------

    # 获取当前程序文件所在的文件夹路径，确保双击运行也能找到文件
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, input_file)
    output_path = os.path.join(current_dir, output_file)

    print(f"--- 正在处理: {input_file} -> {output_file} ---")

    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        print(f"\n[错误] 没找到输入文件：{input_file}")
        print(f"请检查该文件是否和程序放在同一个文件夹下。")
        return

    try:
        count = 0
        with open(input_path, 'r', encoding='utf-8') as f_in, \
             open(output_path, 'w', encoding='utf-8') as f_out:
            
            for line in f_in:
                # 去掉行首尾空格
                line = line.strip()
                if not line:
                    continue
                
                # 1. 移除 # 及其后面的所有备注信息
                clean_data = line.split('#')[0].strip()
                
                # 2. 提取 IP/域名 和 端口
                # rsplit(':', 1) 从右边切分第一个冒号，完美兼容 IPv6 和 域名
                if ':' in clean_data:
                    address, port = clean_data.rsplit(':', 1)
                    
                    # 3. 清理 IPv6 的方括号 []，如果是域名或IPv4则不受影响
                    address = address.replace('[', '').replace(']', '')
                    
                    # 4. 写入文件：地址 + 空格 + 端口 (无其他符号)
                    f_out.write(f"{address} {port}\n")
                    count += 1

        print(f"\n[处理成功!]")
        print(f"转换总数：{count} 条记录")
        print(f"结果已保存到：{output_file}")

    except Exception as e:
        print(f"\n[运行出错]: {e}")

if __name__ == "__main__":
    start_process()
    # 这一行保证了双击运行后窗口不会“一闪而过”
    print("\n" + "="*40)
    input("程序已结束，请按 [回车键] 退出此窗口...")