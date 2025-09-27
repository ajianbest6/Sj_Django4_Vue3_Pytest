<h1 align="center" style="font-family: 'Courier New', monospace; 
          font-size: 48px; 
          color: #00f0ff; 
          padding: 10px; 
          border-radius: 8px; 
          text-shadow: 2px 2px 6px #0ff; 
          letter-spacing: 8px; 
          margin: 0;">
  Sj_Django4_Vue3_Pytest
</h1>
### 演示 demo



### 1. 项目结构目录

```
Sj_Django4_Vue3_Pytest/
├── .github/                        # github配置目录
│   ├── workflows/                  # 工作流
│   └── publish-to-pypi.yaml/       # 发布Pypi配置文件
├── .venv/                          # 虚拟环境目录
├── resource/                       # 图片文档目录
│   ├── docs/                       # 文档目录
│   └── imgs/                       # 图片目录
├── source/                         # 资源存储目录
│   ├── model/                      # 模型存储目录
│   └── video/                      # 视频存储目录
├── src/                            # 源代码目录
│   ├── output/                     # 文件输出目录
│   └── utils/                      # 测试工具目录
├── .flake8                         # flake8 配置文件
├── .gitignore                      # git 忽略文件
├── .pdm-version                    # pdm python 环境版本
├── pdm.lock                        # pdm 依赖库锁定文件
├── LICENSE                         # 开源许可证
├── pyproject.toml                  # uv 依赖库
├── pytest.ini                      # pytest 配置文件
└── README.md                       # 项目说明文档
```

### 2. 快速开始

#### 2.1 安装 PDM

退出虚拟环境，定位到本地环境

```
pip install pdm
```

#### 2.2 初始化环境

```bash
# 安装依赖库
pdm install
```

