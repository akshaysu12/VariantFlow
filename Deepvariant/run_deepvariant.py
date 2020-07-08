#!/usr/bin/env python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import kfp
from kfp import dsl

def run_deepvariant_op(
    input_dir,
    output_dir,
    model_type,
    reference,
    reads,
    output_vcf,
    output_gvcf,
    num_shards
):
  """Creates container for running DeepVariant"""

  return dsl.ContainerOp(
      name='Run DeepVariant',
      image='google/deepvariant:0.10.0',
      command=['/opt/deepvariant/bin/run_deepvariant'],
      arguments=[
          '--model_type', model_type,
          '--ref', reference,
          '--reads', reads,
          '--output_vcf', output_vcf,
          '--output_gvcf', output_gvcf,
          '--num_shards', num_shards]
  )

@dsl.pipeline(
    name='DeepVariant pipeline',
    description='A pipeline for deepvariant.')
def deepvariant_pipeline(
    input_dir,
    output_dir,
    model_type,
    reference,
    reads,
    output_vcf,
    output_gvcf,
    num_shards
):
  """A Pipeline for DeepVariant"""
  run_deepvariant_op(
      input_dir,
      output_dir,
      model_type,
      reference,
      reads,
      output_vcf,
      output_gvcf,
      num_shards)

if __name__ == '__main__':
  kfp.compiler.Compiler().compile(deepvariant_pipeline, __file__ + '.yaml')
