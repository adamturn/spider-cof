import yaml

import handlers
import pipeline
from extract import SeleniumSpider


def main():
    src_dir = handlers.get_src_dir(__file__)

    with open(src_dir / "cfg.yaml") as yaml_stream:
        cfg = yaml.safe_load(yaml_stream)

    spider = SeleniumSpider.construct(
        headless=True,
        user_agent=cfg["extract"]["user_agent"],
        exe_path=cfg["extract"]["chromedriver_path"]
    )

    pipeline.login(spider, cfg)

    return None


if __name__ == "__main__":
    main()
