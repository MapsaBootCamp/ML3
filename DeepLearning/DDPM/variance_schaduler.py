import numpy as np
import matplotlib.pyplot as plt


def variance_schedule(T, s=0.008, max_beta=0.999):
    t = np.arange(T + 1)
    f = np.cos((t / T + s) / (1 + s) * np.pi / 2) ** 2
    alpha = np.clip(f[1:] / f[:-1], 1 - max_beta, 1)
    alpha = np.append(1, alpha).astype(np.float32)  # add α ₀ = 1
    beta = 1 - alpha
    alpha_cumprod = np.cumprod(alpha)
    return alpha, alpha_cumprod, beta  # α ₜ , α̅ ₜ , β ₜ for t = 0 to T


T = 4000
alpha, alpha_cumprod, beta = variance_schedule(T)


print("alpha ", alpha[:4])
print("alpha_cumprod ", alpha_cumprod[:4])
print("beta avaiel ", beta[:10])
print("beta avaset ", beta[2000:2010])
print("beta avakher", beta[-10:])

plt.plot(beta[-100:])
plt.show()
