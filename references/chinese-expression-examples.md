# Contextual Chinese Explanation Examples

Use these only when Chinese wording makes an otherwise sound explanation hard to
follow. They are anonymized, constructed cases, not reports of real systems or
people. The examples illustrate different lengths; no phrasing or structure is
mandatory. Never transfer their hypothetical facts into another answer.

## Short follow-up: same field, changed meaning

**Context:** The user already knows that a task system reads a navigation result.
They now ask why unchanged fields can still cause incompatibility. In this
hypothetical case, the old `success` means the robot has stopped at the goal; the
new `success` means only that the request was received.

**Weaker:** 字段虽未变化，但语义契约遭到破坏，导致系统兼容性下降。

**Better:** 如果原来的“成功”表示机器人已到达并停稳，新版却只表示请求已收到，任务系统即使读到同一个字段，也可能提前执行下一步。

**Why:** It answers the new question in one sentence, identifies what the caller
relies on, and keeps the hypothetical condition visible.

## Paragraph: why choose a midpoint tangent?

**Context:** On `[0,2]`, the user wants to compare the average of `f` with
`f(1)`. They can follow the algebra but do not see why the proof draws a tangent
at `1`. Assume `f` is twice differentiable on the interval and `f'' >= 0` there.

**Weaker:** 利用凸性和区间对称性构造辅助函数，即可得到平均值不等式。

**Better:** 题目要比较整段的平均值与中点值 `f(1)`，所以先找一条容易求平均、又经过 `(1,f(1))` 的线。中点切线是 `T(x)=f(1)+f'(1)(x-1)`；`x-1` 在 `[0,2]` 上的平均值为零，因此切线的平均值正好是 `f(1)`。再用整个区间上的 `f'' >= 0` 得到 `f(x) >= T(x)`，原来两个不同形态的量就可以直接比较了。

**Why:** It connects the target to the chosen construction and states the
condition that makes the curve-tangent comparison valid. It does not repeat a
full proof or replace the technical terms with vague everyday words.

## Fuller explanation: why does a variable-upper-limit integral differentiate?

**Context:** The user knows a definite integral gives an accumulated amount,
but has not connected that amount to its rate of change. Let `G(x)=∫_a^x f(t)dt`;
assume `f` is integrable over the relevant interval and continuous at the
interior point `x`.

**Weaker:** 根据微积分基本定理，变上限积分求导后就是被积函数。

**Better:** `G(x)` 记录从 `a` 累积到 `x` 的量。终点从 `x` 移到 `x+h`，新增的只有这一小段：`G(x+h)-G(x)=∫_x^{x+h} f(t)dt`。所以导数要看这小段累积量除以 `h` 后趋向什么。因为 `f` 在 `x` 附近连续，这一小段上的函数值会接近 `f(x)`；让 `h` 趋近零，商就趋向 `f(x)`，也就是 `G'(x)=f(x)`。这里用到的是终点附近的连续性，不需要先算出整个积分的原函数。

**Why:** It supplies the missing bridge from a small added interval to a
derivative, keeps the continuity condition, and stops after resolving that gap.
