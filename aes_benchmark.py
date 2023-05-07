import aes, os, time

main_key = os.urandom(16)
main_iv = os.urandom(16)

tests_count = 1

def fancy_bench_print(name, data, execution_time_millis, count):
    #print(f"Hello,{name:10s},{name:10s}")
    print(f"{name}+:")
    if type(data) is int:
        print(f"\t{count} times, with data length of {data} bytes")
    else:
        print(f"\t{count} times, with data length of {len(data)} bytes")
    print(f"\tTotal time: {execution_time_millis} milliseconds")
    print(f"\tAverage time: {execution_time_millis/count} milliseconds")

def aes_tests_print(name, data, execution_time_millis, count):
    if type(data) is not int:
        print(f"{name:^16s}/ {count:^12d}/ {len(data):^12d}/ {execution_time_millis:^14.5f}/ {execution_time_millis/count:^14.5f}")
    else:
        print(f"{name:^16s}/ {count:^12d}/ {data:^12d}/ {execution_time_millis:^14.5f}/ {execution_time_millis/count:^14.5f}")


def key_generation_benchmark(count): #generates both key and iv
    start_time = time.perf_counter()
    for _ in range(count):
        key = os.urandom(16)    #generate key
        iv = os.urandom(16)     #generate initialization vector
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    aes_tests_print("generate key+iv", 16, execution_time*1000, count)
    #(f"Time to generate key and iv {count} times is: {execution_time * 1000} milliseconds")
    #print(f"Average for each iteration: {execution_time/count * 1000} milliseconds")

def encryption_benchmark(to_encrypt, count):
    start_time = time.perf_counter()
    for _ in range(count):
        encrypted = aes.AES(main_key).encrypt_ctr(to_encrypt, main_iv)
    #print(f"Encrypted: {bin(int.from_bytes(encrypted, byteorder='big')).strip('0b')}")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    aes_tests_print("encrypt", to_encrypt, execution_time * 1000, count)
    #print(f"Time taken to encrypt {count} is: {execution_time * 1000} milliseconds")
    #print(f"Average for each iteration: {execution_time / count * 1000} milliseconds")

def decryption_benchmark(to_decrypt, count):
    start_time = time.perf_counter()
    for _ in range(count):
        decrypted = aes.AES(main_key).decrypt_ctr(to_decrypt, main_iv)
    #print(f"Decrypted: {decrypted.decode('utf - 8')}")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    aes_tests_print("decrypt", to_decrypt, execution_time * 1000, count)
    #print(f"Time taken to decrypt {count} is: {execution_time * 1000} milliseconds")
    #print(f"Average for each iteration: {execution_time / count * 1000} milliseconds")

print(f"{'operation':^16s}/ {'count':^12s}/ {'data size':^12s}/ {'total time ms':^14s}/ {'avg time ms':^14s}")
key_generation_benchmark(tests_count)
print()

encryption_benchmark(os.urandom(5), tests_count)
decryption_benchmark(os.urandom(5), tests_count)
print()

encryption_benchmark(os.urandom(10), tests_count)
decryption_benchmark(os.urandom(10), tests_count)
print()

encryption_benchmark(os.urandom(25), tests_count)
decryption_benchmark(os.urandom(25), tests_count)
print()

encryption_benchmark(os.urandom(100), tests_count)
decryption_benchmark(os.urandom(100), tests_count)
print()

encryption_benchmark(os.urandom(200), tests_count)
decryption_benchmark(os.urandom(200), tests_count)
print()

encryption_benchmark(os.urandom(500), tests_count)
decryption_benchmark(os.urandom(500), tests_count)
print()

encryption_benchmark(os.urandom(1000), tests_count)
decryption_benchmark(os.urandom(1000), tests_count)
print()

encryption_benchmark(os.urandom(10000), tests_count)
decryption_benchmark(os.urandom(10000), tests_count)
print()

encryption_benchmark(os.urandom(100000), tests_count)
decryption_benchmark(os.urandom(100000), tests_count)
print()
