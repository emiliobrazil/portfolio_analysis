import CL_finance as fnc

syb = 'PETR4'
print(f"{syb} is valid? {fnc.is_valid(syb)}")

print(fnc.history([syb], "2020-10-01", "2023-10-21", '1mo'))

