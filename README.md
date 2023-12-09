# stable-diffusion-quantized

- [1.Getting Started](#1-getting-started)
- [2.Input prompt](#2-input-prompt)
- [3.Configuation](#3-configuation)

## 1. Getting Started
```bash
docker run -it lowinli98/stable-diffusion-quantized:v0.1 -v ./volume:/app/output
```

```docker
/app/env/bin/python inference.py
```

## 2. Input prompt

```docker
/app/env/bin/python inference.py -p "portrait photo headshot by mucha, sharp focus, elegant, render, octane, detailed, award winning photography, masterpiece, rim lit"
```

## 3. Configuation

```
vim config.py
```