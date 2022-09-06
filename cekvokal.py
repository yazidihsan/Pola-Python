

x = input("Masukkan kalimat:" .lower())

huruf_vokal = {
    'a': 0,
    'i': 0,
    'u': 0,
    'e': 0,
    'o': 0
}

total_huruf_vokal = 0

for karakter in x:
    if karakter in ['a', 'i', 'u', 'e', 'o']:
        huruf_vokal[karakter] += 1
        total_huruf_vokal += 1

print(f'jumlah karakter ada : {len(x)}')
print(f"jumlah huruf vokal ada : {total_huruf_vokal}")
print(f"""\t
    'a' => {huruf_vokal['a']},
    'i' => {huruf_vokal['i']},
    'u' => {huruf_vokal['u']},
    'e' => {huruf_vokal['e']},
    'o' => {huruf_vokal['o']}
      """)
