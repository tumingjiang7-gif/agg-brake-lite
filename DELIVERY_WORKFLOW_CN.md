# AGG Brake Lite 手动交付流程

## 用户侧

1. 扫微信收款码
2. 付款 `19.9 元`
3. 备注：`AGG Brake + 邮箱`
4. 把付款截图发到：`642635193@qq.com`

## 你这边

1. 确认截图和邮箱
2. 导出创始试点交付包：

```bash
python scripts/export_pilot_bundle.py
```

3. 把导出的 zip 包发给对方
4. 引导对方先看：
   - `README.md`
   - `FAQ.md`
   - `FEEDBACK_TEMPLATE.md`

## 后续反馈入口

如果对方真的接入了：

- 优先让对方用 `FEEDBACK_TEMPLATE.md`
- 如果愿意，再让对方导出匿名日志

## 当前原则

- 先跑 observe
- 不承诺生产兜底
- 不做高触达陪跑
- 只收窄在 checkout / payment 邻域
