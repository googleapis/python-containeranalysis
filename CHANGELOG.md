# Changelog

## [1.0.5](https://github.com/googleapis/python-containeranalysis/compare/v1.0.4...v1.0.5) (2022-06-07)


### Bug Fixes

* **deps:** require protobuf<4.0.0 on v1 branch ([#296](https://github.com/googleapis/python-containeranalysis/issues/296)) ([87ce6a6](https://github.com/googleapis/python-containeranalysis/commit/87ce6a6fed7888f17f10ef08e12405ad97bff549))

### [1.0.4](https://github.com/googleapis/python-containeranalysis/compare/v1.0.3...v1.0.4) (2022-04-04)


### Bug Fixes

* **deps:** require google-api-core >= 1.31.5, >= 2.3.2 on v1 release ([#260](https://github.com/googleapis/python-containeranalysis/issues/260)) ([be6fb87](https://github.com/googleapis/python-containeranalysis/commit/be6fb87d6d3e00d798b37dc89324ca88d3da6107))

### [1.0.3](https://www.github.com/googleapis/python-containeranalysis/compare/v1.0.2...v1.0.3) (2020-08-11)


### Bug Fixes

* Use different versions of pytest for python 2 and python3 [([#2558](https://www.github.com/googleapis/python-containeranalysis/issues/2558))](https://github.com/GoogleCloudPlatform/python-docs-samples/issues/2558) ([7d21641](https://www.github.com/googleapis/python-containeranalysis/commit/7d21641eb50f574784ae7dfbb1d25a0d0af14699))
* **deps:** add upper bound for grafeas ([#30](https://www.github.com/googleapis/python-containeranalysis/issues/30)) ([5ca8f79](https://www.github.com/googleapis/python-containeranalysis/commit/5ca8f7981349ed86438185f02681225f059cc9d9))

### [1.0.2](https://www.github.com/googleapis/python-containeranalysis/compare/v1.0.1...v1.0.2) (2020-07-16)


### Bug Fixes

* update retry config ([#23](https://www.github.com/googleapis/python-containeranalysis/issues/23)) ([ddf9585](https://www.github.com/googleapis/python-containeranalysis/commit/ddf95852778c0e60961516ecd77b793e6af3295b))


### Documentation

* add multiprocessing note ([#21](https://www.github.com/googleapis/python-containeranalysis/issues/21)) ([be29088](https://www.github.com/googleapis/python-containeranalysis/commit/be290885cef76ffdd27afb44cd858c6a89d4f280))

### [1.0.1](https://www.github.com/googleapis/python-containeranalysis/compare/v1.0.0...v1.0.1) (2020-06-16)


### Bug Fixes

* fix `release_status` in `setup.py` ([#17](https://www.github.com/googleapis/python-containeranalysis/issues/17)) ([2de847c](https://www.github.com/googleapis/python-containeranalysis/commit/2de847c1cf0e3e9a4f09f35d7abb5004dcee6bad))

## [1.0.0](https://www.github.com/googleapis/python-containeranalysis/compare/v0.3.1...v1.0.0) (2020-06-16)


### Features

* release as production/stable ([#15](https://www.github.com/googleapis/python-containeranalysis/issues/15)) ([b81e207](https://www.github.com/googleapis/python-containeranalysis/commit/b81e2074eb86c015c781b79a68839cbaeb40e5b2))
* remove `note_path` and `occurence_path` (via synth) ([#7](https://www.github.com/googleapis/python-containeranalysis/issues/7)) ([656b11e](https://www.github.com/googleapis/python-containeranalysis/commit/656b11eee22f11d1109e288190fc63b6c8ff20b7))

## 0.3.1

11-07-2019 11:08 PST

**NOTE**: Please upgrade to this version if you will also be using `google-cloud-build`. 

### Implementation Changes
- Make google.cloud.devtools a namespace ([#9606](https://github.com/googleapis/google-cloud-python/pull/9606))

### Documentation
- Change requests intersphinx ref (via synth)
- Fix intersphinx reference to requests ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Remove CI for gh-pages, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))

## 0.3.0

08-12-2019 13:53 PDT

### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8948](https://github.com/googleapis/google-cloud-python/pull/8948))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Normalize docs. ([#8994](https://github.com/googleapis/google-cloud-python/pull/8994))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 0.2.0

07-12-2019 16:56 PDT

### New Features
- Add 'client_options' support (via synth). ([#8502](https://github.com/googleapis/google-cloud-python/pull/8502))
- Add 'options_' argument to clients' 'get_iam_policy'; pin black version (via synth). ([#8653](https://github.com/googleapis/google-cloud-python/pull/8653))

### Dependencies
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))

### Documentation
- Update READMEs. ([#8456](https://github.com/googleapis/google-cloud-python/pull/8456))

### Internal / Testing Changes
- Fix language in repo metadata. ([#8537](https://github.com/googleapis/google-cloud-python/pull/8537))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))

## 0.1.0

06-19-2019 11:02 PDT

### New Features
- Initial release of Container Analysis client library. ([#8381](https://github.com/googleapis/google-cloud-python/pull/8381))
