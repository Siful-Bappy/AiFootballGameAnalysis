"""
football_ai/
│
├── data/
│   ├── raw/                  # Raw match videos
│   ├── processed/            # Processed frames
│   └── annotations/          # Labels / annotations
│
├── models/
│   ├── weights/              # YOLO weights (.pt files)
│   └── trained/              # Your trained models
│
├── src/
│   ├── detection/            # Player & ball detection
│   ├── tracking/             # Object tracking
│   ├── analysis/             # Tactical analysis
│   └── visualization/        # Draw annotations
│
├── notebooks/                # Jupyter experiments
├── outputs/                  # Result videos/reports
├── config.yaml               # All configs here
├── requirements.txt
├── main.py
└── README.md

python -m ipykernel install --user --name=football_ai --display-name "Football AI"
jupyter notebook

"""