
from colas_simulator import mm1, mms, mmsk, mg1, mek1

# Test M/M/1
la = 40
mi = 30
l, lq, w, wq, rho = mm1(la, mi)
print("l:", l, ", lq:", lq, ", w:", w, ", wq:", wq)
print("l:", float(l), ", lq:", float(lq), ", w:", float(w), ", wq:", float(wq))
print("ROUND", round(float(wq), 2))


# Test M/M/s
la = 40
mi = 30
s = 2
l, lq, w, wq, rho = mms(la, mi, s)
print("l:", l, ", lq:", lq, ", w:", w, ", wq:", wq)
print("l:", float(l), ", lq:", float(lq), ", w:", float(w), ", wq:", float(wq))


# Test M/M/s/K
la = 40
mi = 30
s = 2
k = 10
lae, l, lq, w, wq, rho = mmsk(la, mi, s, k)
print("lae:", lae, ", l:", l, " lq:", lq, ", w:", w, ", wq:", wq)
print("lae:", float(lae), ", l:", float(l), ", lq:", float(lq), ", w:", float(w), ", wq:", float(wq))

# Test M/G/1
la = 20
mi = 30
sig = 1/5
l, lq, w, wq, rho = mg1(la, mi, sig)
print("l:", l, " lq:", lq, ", w:", w, ", wq:", wq)
print("l:", float(l), ", lq:", float(lq), ", w:", float(w), ", wq:", float(wq))

# Test M/Ek/1
la = 20
mi = 30
k = 4
l, lq, w, wq, rho = mek1(la, mi, sig)
print("l:", l, " lq:", lq, ", w:", w, ", wq:", wq)
print("l:", float(l), ", lq:", float(lq), ", w:", float(w), ", wq:", float(wq))
