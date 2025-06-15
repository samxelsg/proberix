
jurnal = [
    {'tanggal': '2024-01-01', 'akun': 'Kas', 'debit': 100_000_000, 'kredit': 0},
    {'tanggal': '2024-01-01', 'akun': 'Mobil (Transportasi)', 'debit': 150_000_000, 'kredit': 0},
    {'tanggal': '2024-01-01', 'akun': 'Modal', 'debit': 0, 'kredit': 250_000_000},
    {'tanggal': '2024-01-12', 'akun': 'Beban Service Mobil', 'debit': 700_000, 'kredit': 0},
    {'tanggal': '2024-01-12', 'akun': 'Hutang', 'debit': 0, 'kredit': 700_000},
    {'tanggal': '2024-01-23', 'akun': 'Kas', 'debit': 50_000_000, 'kredit': 0},
    {'tanggal': '2024-01-23', 'akun': 'Modal', 'debit': 0, 'kredit': 50_000_000},
    {'tanggal': '2024-01-25', 'akun': 'Beban Gaji', 'debit': 10_000_000, 'kredit': 0},
    {'tanggal': '2024-01-25', 'akun': 'Kas', 'debit': 0, 'kredit': 10_000_000},
    {'tanggal': '2024-01-27', 'akun': 'Hutang', 'debit': 500_000, 'kredit': 0},
    {'tanggal': '2024-01-27', 'akun': 'Kas', 'debit': 0, 'kredit': 500_000},
    {'tanggal': '2024-01-28', 'akun': 'Kas', 'debit': 6_000_000, 'kredit': 0},
    {'tanggal': '2024-01-28', 'akun': 'Pendapatan Jasa', 'debit': 0, 'kredit': 6_000_000},
    {'tanggal': '2024-01-30', 'akun': 'Prive', 'debit': 2_000_000, 'kredit': 0},
    {'tanggal': '2024-01-30', 'akun': 'Kas', 'debit': 0, 'kredit': 2_000_000},
    {'tanggal': '2024-01-30', 'akun': 'Beban Utilitas', 'debit': 1_000_000, 'kredit': 0},
    {'tanggal': '2024-01-30', 'akun': 'Kas', 'debit': 0, 'kredit': 1_000_000},
    {'tanggal': '2024-01-30', 'akun': 'Beban Asuransi', 'debit': 1_500_000, 'kredit': 0},
    {'tanggal': '2024-01-30', 'akun': 'Kas', 'debit': 0, 'kredit': 1_500_000},
]


from collections import defaultdict

t_accounts = defaultdict(lambda: {'debit': 0, 'kredit': 0})

for entry in jurnal:
    akun = entry['akun']
    t_accounts[akun]['debit'] += entry['debit']
    t_accounts[akun]['kredit'] += entry['kredit']


trial_balance = []

for akun, saldo in t_accounts.items():
    debit = saldo['debit']
    kredit = saldo['kredit']
    trial_balance.append({'akun': akun, 'debit': debit, 'kredit': kredit})


print("Jurnal Umum:")
for entry in jurnal:
    print(entry)

print("\nT-Accounts:")
for akun, saldo in t_accounts.items():
    print(f"{akun}: Debit = {saldo['debit']}, Kredit = {saldo['kredit']}")

print("\nTrial Balance:")
for entry in trial_balance:
    print(entry)
