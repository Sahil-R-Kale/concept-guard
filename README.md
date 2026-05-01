# ConceptGuard

## Overview
ConceptGuard is a benchmark for evaluating *concept-level unlearning* in Large Language Models (LLMs). It focuses on **dual-use concepts**—those that can appear in both harmful and benign contexts—and measures whether models can suppress harmful behavior while preserving useful knowledge.

## Abstract
Large Language Models (LLMs) increasingly require selective removal of harmful or sensitive knowledge, called unlearning, yet existing methods and benchmarks fail to evaluate this capability completely. Current approaches rely on disjoint forget and retain sets composed of independent facts, and measure success using simple factual recall. This fails to capture a key requirement of unlearning: eliminating harmful behaviors while preserving beneficial knowledge.  

We introduce **ConceptGuard**, a benchmark built around *dual-use concepts*, where forget and retain sets are complementary and evaluation is context-sensitive. Our goal is to measure and improve **contextual separation**—the ability to suppress harmful usage of a concept while retaining benign usage. Experiments show that existing unlearning methods struggle under this setting, revealing fundamental limitations and motivating more robust, concept-aware approaches.

## Main Goal
Enable and evaluate **fine-grained, concept-level unlearning** that:
- Removes harmful applications of knowledge
- Preserves benign and useful usage
- Improves contextual separation in model behavior

## Dataset
The complete dataset is provided in the `data/` directory.  
It includes:
- Forget set (harmful usage)
- Retain set (benign usage)
- Organized by dual-use concepts

## Setup & Usage

This repository builds on the Open-Unlearning framework.

### 1. Base Setup
Follow setup instructions from:
https://github.com/locuslab/open-unlearning/blob/main/docs/experiments.md

### 2. Running Experiments

Use the provided configs in the `configs/` folder:

- **Fine-tuning:**
  ```
  cg_finetune.yaml
  ```

- **Unlearning:**
  ```
  cg_unlearn.yaml
  ```

Override parameters as needed following Open-Unlearning instructions.

## Notes
- All experiments follow the same pipeline as Open-Unlearning.
- Only configuration files need to be swapped to reproduce results.
- Hyperparameters can be overridden via CLI or config edits.
